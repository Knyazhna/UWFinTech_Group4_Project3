//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// ERC721 is a standard for representing ownership of non-fungible tokens, that is, where each token is unique.
// Ownable represents ownership by account that deployed the NFT contract
// SafeMath revertS a transaction when an operation overflows.

import '@openzeppelin/contracts/access/Ownable.sol';
import '@openzeppelin/contracts/utils/Counters.sol';
import '@openzeppelin/contracts/utils/math/SafeMath.sol';
import '@openzeppelin/contracts/token/ERC721/ERC721.sol';

contract Nft721 is ERC721, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

// Use counters to keep track of tokens given during the event.
// When you say using safemath for uint256 means that it will never overflow unless you pass a 255, but it will not because it will be represented within SafeMath as a uint256 .

    Counters.Counter private _tokenIds;

    uint public constant MAX_SUPPLY = 1;

    constructor() ERC721("RSVPCreator", "RSVP") {
        _mintSingleNFT();
    } 

    function _mintSingleNFT() private {
        uint newTokenID = _tokenIds.current();
        _safeMint(address(this), newTokenID);
        _tokenIds.increment();
    }

    function setApprovalForContract(address operator, bool approved) external {
        _setApprovalForAll(address(this),operator, approved);
    }

    function setApprovalForCreator(address creator, address _contract, bool approved) external {
        _setApprovalForAll(creator, _contract, approved);
    }
}


// CITATION : Nakglom,Saravut (2022 , February 6) Github. solidity-avalanche-RSVP-staking-event/contracts/CreatorERC721.sol 
//             https://github.com/SRVng/solidity-avalanche-RSVP-staking-event/blob/ec4c5ed57fc6edff239395e8b7dfa2b387e1bd82/contracts/CreatorERC721.sol
