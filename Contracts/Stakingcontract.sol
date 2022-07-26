// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

//  Import the following contracts from the OpenZeppelin library:
//    * `SafeMath` is a solidity math library especially designed to support safe math operations: safe means that it prevents overflow when working with uint.
//    * `ERC20DBurnable` Allow token holders to destroy their own tokens prior to event in case of cancellation.
//    * `AccessControl` Contract module that allows granting role-based access control mechanisms.
//    * `IERC721, IERC720` import interfaces from openzeppelin.

// import './RSVP_Event.sol';
import '@openzeppelin/contracts/token/ERC721/IERC721.sol';
import '@openzeppelin/contracts/token/ERC20/IERC20.sol';
import '@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol';
import '@openzeppelin/contracts/access/AccessControl.sol';
import '@openzeppelin/contracts/utils/math/SafeMath.sol';
import '@openzeppelin/contracts/access/Ownable.sol';
import '@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol';
//import 'hardhat/console.sol';
import './RewardToken.sol';

interface IRewardToken is IERC20 {
    function mint(address to, uint256 amount) external;
}


contract StakingSystem is Ownable, ERC721Holder {
    IRewardToken public rewardsToken;
    IERC721 public nft;

    //State Variables
    uint256 public stakedTotal;
    uint256 public stakingStartTime;
    uint256 constant stakingTime = 180 seconds; // set staking time as 180 seconds, but to reduce time stamp risk is better to use larger amounts of time like days.
    uint256 constant token = 10e18; // Token has 18 decimals
    
    //Create struct to keep the detail of depositor.
    struct Staker {
        uint256[] tokenIds; // tokenIds is that the user is using for the staking.
        mapping(uint256 => uint256) tokenStakingCoolDown; // mapping for track the token index.
        uint256 balance; // the balance of the user
        uint256 rewardsReleased; // the clamied rewards by the user.
    }


    /// Other variables
    /// @notice mapping of a staker to its wallet
    mapping(address => Staker) public stakers; // to store token value of an address

    /// @notice Mapping from token ID to owner address

    mapping(uint256 => address) public tokenOwner;
    bool public tokensClaimable;
    bool initialised;

    /// Events variables
    /// @notice event emitted when a user has staked a nft

    event Staked(address owner, uint256 amount);

    /// @notice event emitted when a user has unstaked a nft
    event Unstaked(address owner, uint256 amount);

    /// @notice event emitted when a user claims reward
    event RewardPaid(address indexed user, uint256 reward);

    /// @notice Allows reward tokens to be claimed
    event ClaimableStatusUpdated(bool status);

    /// @notice Emergency unstake tokens without rewards
    event EmergencyUnstake(address indexed user, uint256 tokenId);

    /// Staking Function

    function initStaking() public onlyOwner {
        //needs access control
        //If initialised is not false, then return "Already initialised"
        require(!initialised, "Already initialised");
        stakingStartTime = block.timestamp;
        initialised = true;
    }

    function setTokensClaimable(bool _enabled) public onlyOwner {
        //needs access control
        tokensClaimable = _enabled;
        emit ClaimableStatusUpdated(_enabled); // to log the transactions "Claimable status update"
    }

    function getStakedTokens(address _user)
        public
        view
        returns (uint256[] memory tokenIds)
    {
        return stakers[_user].tokenIds; // return user tokenID
    }

    function stake(uint256 tokenId) public {
        _stake(msg.sender, tokenId); // calling private stake function
    }

    function stakeBatch(uint256[] memory tokenIds) public {
        for (uint256 i = 0; i < tokenIds.length; i++) { // traverse entire tokenID array for mass update, arrayLength
            _stake(msg.sender, tokenIds[i]);
        }
    }

    function _stake(address _user, uint256 _tokenId) internal {
        require(initialised, "Staking System: the staking has not started");
        require(
            nft.ownerOf(_tokenId) == _user,
            "user must be the owner of the token"
        );
        Staker storage staker = stakers[_user];

        staker.tokenIds.push(_tokenId); // adding tokenId to array
        staker.tokenStakingCoolDown[_tokenId] = block.timestamp;
        tokenOwner[_tokenId] = _user;
        nft.approve(address(this), _tokenId);
        nft.safeTransferFrom(_user, address(this), _tokenId);

        emit Staked(_user, _tokenId);
        stakedTotal++; // increment total number of staked
    }

    function unstake(uint256 _tokenId) public {
        claimReward(msg.sender);
        _unstake(msg.sender, _tokenId);
    }

    function unstakeBatch(uint256[] memory tokenIds) public { // unstake entire array , total tokenId
        claimReward(msg.sender);
        for (uint256 i = 0; i < tokenIds.length; i++) {
            if (tokenOwner[tokenIds[i]] == msg.sender) {
                _unstake(msg.sender, tokenIds[i]);
            }
        }
    }

    // Unstake without caring about rewards. EMERGENCY ONLY.
    function emergencyUnstake(uint256 _tokenId) public {
        require(
            tokenOwner[_tokenId] == msg.sender,
            "nft._unstake: Sender must have staked tokenID"
        );
        _unstake(msg.sender, _tokenId);
        emit EmergencyUnstake(msg.sender, _tokenId);
    }

    function _unstake(address _user, uint256 _tokenId) internal {
        require(
            tokenOwner[_tokenId] == _user,
            "Nft Staking System: user must be the owner of the staked nft"
        );
        Staker storage staker = stakers[_user];
        
        if (staker.tokenIds.length > 0) {
            staker.tokenIds.pop(); // empty out entire array
        }
        staker.tokenStakingCoolDown[_tokenId] = 0; 
        delete tokenOwner[_tokenId];

        nft.safeTransferFrom(address(this), _user, _tokenId);

        emit Unstaked(_user, _tokenId);
        stakedTotal--; // decrement total number of staked
    }

    function updateReward(address _user) public {

        // the logic of the update function is checking if the token is staked (the cooldown will be 0 if not).
        // if the token is staked, need to check how many stacking cycles are completed.
        
        Staker storage staker = stakers[_user];
        uint256[] storage ids = staker.tokenIds;
        for (uint256 i = 0; i < ids.length; i++) {
            if (
                staker.tokenStakingCoolDown[ids[i]] <
                block.timestamp + stakingTime &&
                staker.tokenStakingCoolDown[ids[i]] > 0
            ) {
            
                uint256 stakedDays = ((block.timestamp - uint(staker.tokenStakingCoolDown[ids[i]]))) / stakingTime; // caculate remaining day
                uint256 partialTime = ((block.timestamp - uint(staker.tokenStakingCoolDown[ids[i]]))) % stakingTime; // caculate remaining time
                
                staker.balance +=  token * stakedDays;

                staker.tokenStakingCoolDown[ids[i]] = block.timestamp + partialTime;

                //console.logUint(staker.tokenStakingCoolDown[ids[i]]); 
                //console.logUint(staker.balance);
            }
        }
    }

// claim reward will mint the tonkens to the user.
    function claimReward(address _user) public {
        require(tokensClaimable == true, "Tokens cannnot be claimed yet");
        require(stakers[_user].balance > 0 , "0 rewards yet");


        stakers[_user].rewardsReleased += stakers[_user].balance;
        stakers[_user].balance = 0;
   
        rewardsToken.mint(_user, stakers[_user].balance); // distribute reward balance to user

        emit RewardPaid(_user, stakers[_user].balance);
    }
}