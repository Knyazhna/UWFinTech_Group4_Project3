# Project 3: Event Staking
In this project we will utilize smart contracts and minted tokens to create incentive for event attendance after an RSVP.
*   [Sample Staking Repo](https://github.com/SRVng/solidity-avalanche-RSVP-staking-event)


## Technologies
* Brownie
* Solidity


## Outline
### NFT Staking System
1.  An Erc20 token will be the reward token.
2.  An Erc721 will be the nft token.
3.  The staking contract will hold the staked nft and will allow claiming the rewards.

### Outline Completion Steps (Draft) 
1. Create erc20 token using Zeppelin contracts
2. Create NFT contract
3. On Stake system:
	1. Use interface to call the functions
4. Add mint function
5. Add utility variables
6. Create struct to:
	1. Keep info of Staker entities
	2. Events
	3. Other functions as we see fit
	4. Control contract
	5. Get Functioin
7. Create stake function
	1. Double check owner status
	2. Use Web3 to transfer rights
8. Make usStake
9. Make claim
10. Update
11. Reward

