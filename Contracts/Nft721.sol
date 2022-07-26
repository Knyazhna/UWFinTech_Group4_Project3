
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;


//ERC721 is a standard for representing ownership of non-fungible tokens, that is, where each token is unique.
//ERC721Burnable: A way for token holders to burn their own tokens.
//AccessControl provides a general role based access control mechanism. Multiple hierarchical roles can be created and assigned each to multiple accounts.
//SafeMath revertS a transaction when an operation overflows.




import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";



contract Nft721 is  ERC721, ERC721Burnable,  AccessControl{



     //When you say using Counters for Counters.Counter, it means that we assign all the functions inside the Counters library, like current() or increment(), to the Counter struct.
     //When you say using safemath for uint256 means that it will never overflow unless you pass a 255, but it will not because it will be represented within SafeMath as a uint256 .

 
    using Counters for Counters.Counter;
    using SafeMath for uint256;


     //Roles are referred to by their bytes32 identifier. These should be exposed in the external API and be unique. The best way to achieve this is by using public constant hash (keccak256)digests:

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    Counters.Counter private _tokenIdCounter;
    uint public constant MAX_SUPPLY = 1;


     //constructor Initializes the contract setting the deployer as the initial owner.
     //_grantRole(bytes32 role, address account) Grants role to account.Internal function without access restriction.   
     //DEFAULT_ADMIN_ROLE  means that only accounts with this role will be able to grant or revoke other roles. More complex role relationships can be created by


    constructor() ERC721("RSVPToken", "RSVP") {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
    }


    // _baseURI  is called by other functions.We  override it so it returns the correct thing.Override the function and return some string variable you have control over.


     function _baseURI() internal pure override returns (string memory) {
        return "ipfs::/ipfs_link/";
    }

    //The _safeMint flavor of minting causes the recipient of the tokens, if it is a smart contract, to react upon receipt of the tokens.Safemint has extra features than mint.
 
 
    function safeMint(address to) public onlyRole(MINTER_ROLE) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    // The following functions are overrides required by Solidity.

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, AccessControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
