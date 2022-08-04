// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EventSafe {
    
    //State-Variable
    uint256 private constant fee = 0.1 ether; // 100m gwei
    
    //Mapping
    mapping(address => bool) depositor;
    
    //Function to make sure attendees have paid their stake
    function deposit() internal returns(uint256 collateral) {
        require(depositor[msg.sender] == true, "Error: 1");
        bool currency_check = false;
        
        if (msg.value == fee) {
            currency_check = true;
        }
        
        require(currency_check == true, "Please pay 0.1 ETH");
        depositor[msg.sender] = false;
        
        
        return address(this).balance;
    }
    // extra security ensuring they are paying from the right wallet
    function return_collateral(address payable wallet) internal {
        require(wallet == msg.sender, "You cannot withdraw others wallet");
        wallet.transfer(fee);
    }
    
    //Event
    event LogCollateral(string description,address creator);
}

// CITATION : Nakglom,Saravut (2022 , February 6) Github. solidity-avalanche-RSVP-staking-event/contracts/EventSafe.sol
//            https://github.com/SRVng/solidity-avalanche-RSVP-staking-event/blob/main/contracts/EventSafe.sol