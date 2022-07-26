// SPDX-License-Identifier: SEE LICENSE IN LICENSE

pragma solidity ^0.8.1;

//  Import the following contracts from the OpenZeppelin library:
//    * `ERC20` Create a fungible reward token.
//    * `ERC20DBurnable` Allow token holders to destroy their own tokens prior to event in case of cancellation.
//    * `AccessControl` Contract module that allows granting role-based access control mechanisms. 
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract RewardToken is ERC20, ERC20Burnable, AccessControl {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

// keccak256 - Hashing function
// bytes32 - Roles are referred to by their bytes32 identifier(exposed in external API)
    
    constructor() ERC20("RewardToken", "RDW") {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
    }

//The admin role for all roles is DEFAULT_ADMIN_ROLE, which means that only accounts with this role will be able to grant or revoke other roles
//The DEFAULT_ADMIN_ROLE is also its own admin: it has permission to grant and revoke this role.
    
    function mint(address to, uint256 amount) public{
        _mint(to, amount);
    }

      function approveFromContract(address owner,address spender, uint256 amount) public returns(bool) {        
        _approve(owner, spender, amount);
        return true;
    }
}