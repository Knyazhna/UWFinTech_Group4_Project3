// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity  ^0.5.0;

// imports go here ~
import './RewardToken.sol';

// Goal: write a contract that will allow a person to create an event and check people in; allow people
// to pay a small amount to RSVP and if they don't show up then the reservation amount gets redistributed to all attendees.
// TODO: import other contracts & change variable names

contract RSVP_Event is Staking,EventSafe {
    using SafeMath for uint256;

    //Predefined value in enum
    enum EventStatus {Waiting, Ended}

    //Save enum status in variable

    //Launch this event when status is updated
    event LogEvent(string event_name,string description);
    event LogRSVP(address participant);
    
    //state variable
    string[] internal OngoingEvent;
    Event_Detail public event_details;
    EventStatus public event_status;
    CreatorERC721 public creatorERC721;
    address public owner;
    
    //struct
    struct Event_Detail {
        string event_name;
        uint256 time_start;
        uint256 time_end;
        address creator;
    }
    
    //mapping
    mapping(address => bool) attendance;

    //When running the contract there should not be any ongoing events
    constructor(RewardToken reward, CreatorERC721 _creatorERC721, address _owner) Staking(reward) {
        event_status = EventStatus.Ended;
        creatorERC721 = _creatorERC721;
        owner = _owner;
    }
    
    function RSVP_Create(string memory event_name, uint256 time_end, uint256 _stake) public payable {
        //Pay an ether
        require(OngoingEvent.length == 0, "RSVP event can occur only one at a time");
        depositor[msg.sender] = true;
        deposit();
        
        //Create an event
        event_details = Event_Detail(event_name,block.timestamp,time_end, msg.sender);
        event_status = EventStatus.Waiting;
        OngoingEvent.push(event_name);

        //NFT Contract
        getNFTfromContract();
        giveCreatorNFT(msg.sender);
        
        //Stake
        RSVP(_stake);
        emit LogEvent(event_name,"RSVP Event Created");
    }

    function getNFTfromContract() private {
        creatorERC721.setApprovalForContract(address(this), true);
        creatorERC721.transferFrom(address(creatorERC721), address(this), 0);
    }

    function giveCreatorNFT(address creator) private {
        creatorERC721.transferFrom(address(this), creator, 0);
        creatorERC721.setApprovalForCreator(tx.origin, address(this), true);
    }
    
    function ongoing_event() public view returns(string memory event_name, uint256 start_from, uint256 until, address creator) {
        return (event_details.event_name, event_details.time_start, event_details.time_end, event_details.creator);
    }

    function event_creator() public view returns(address) {
        return event_details.creator;
    }
    
    function end_time() external view returns(uint256 until) {
        return event_details.time_end;
    }
    
    function RSVP(uint256 _stake) public {
        require(event_status == EventStatus.Waiting, "There's no ongoing event");
        require(block.timestamp < event_details.time_end || creatorERC721.balanceOf(msg.sender) == 1, "It's check in period");
        stake_once[msg.sender] = true;
        
        deposit_stake(_stake);

        attendance[msg.sender] = false;
        emit LogRSVP(msg.sender);
    }
    
    function Check_in() public {
        require(block.timestamp > event_details.time_end  && 
                block.timestamp <= (event_details.time_end + checked_in_period), 
                "The check-in period didn't start or you missed it, please check the event detail");
        require(attendance[msg.sender] == false, "You already check-in");
        
        withdraw_stake();
        attendance[msg.sender] = true;
    }
    
    function RSVP_End(address payable your_address) public returns(uint256 shared_amount) {
        require(creatorERC721.balanceOf(msg.sender) == 1, "The Creator only");
        require(block.timestamp > (event_details.time_end + checked_in_period), "Please wait");
        
        (uint256 _digits,) = reward_share();
        return_collateral(your_address);
        getNFTback(false);
        
        delete event_details;
        event_status = EventStatus.Ended;
        OngoingEvent.pop();
        
        return(_digits);
    }

    function getNFTback(bool isOwner) private {
        if (!isOwner) {
            creatorERC721.transferFrom(tx.origin, address(creatorERC721), 0);
            creatorERC721.setApprovalForCreator(event_details.creator, address(this), false);
        } else {
            creatorERC721.transferFrom(event_details.creator, address(creatorERC721), 0);
            creatorERC721.setApprovalForCreator(event_details.creator, address(this), false);
        }
    }

    // This function should be removed in production
    function Force_End(address payable your_address) public returns(uint256 shared_amount) {
        require(creatorERC721.balanceOf(msg.sender) == 1 || msg.sender == owner, "The Creator only");
        
        (uint256 _digits,) = reward_share();
        return_collateral(your_address);
        getNFTback(true);
        
        delete event_details;
        event_status = EventStatus.Ended;
        OngoingEvent.pop();
        
        return(_digits);
    }
}