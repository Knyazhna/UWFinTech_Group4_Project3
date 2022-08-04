# Project 3: Event Staking
![](Resources/hero.png)
In this project we will utilize smart contracts and minted tokens to create incentive for event attendance after an RSVP.


## Problem Statement:
In this post-COVID era, attempting to arrange events both virtually and in-person, has become an increasingly daunting task. 

There are many individuals show initial interest by casually RSVPing to a hosted event; however when the time comes, a fraction, if not a majority, do not attend. This creates a strenuous situation for hosts especially when others are involved such as guest speakers, bands, etc.

In light of these embarassing and far too frequent attendance issues, we have created our last project to inspire hope in those hosts selfless enough to bring people back together [safely]. 

### Problem
Inconsistent event attendance promises in a post-COVID era, creating volatility for hosts thus, decreasing event satisfaction and decentivizing hosts.

### Solution
A Solidity, smart contract supported, event planning platform in which guests RSVP and pay a small amount to a decentralized fund. The inidividuals who RSVP but fail to check in, lose their staked ETH; those who do attend, get their money back and a share of the reward.

### Project Goal
Our goal is to learn Solidtiy by taking an in-depth understanding of various Solidty contracts. We followed instructions of online tutorial and public code repository 
to integrate Solidity contracts complie and deployed with Ganache, Metamask and Javascript to provide a front-end experience.

Developed index.html as a webpage to host information. Created index.css to provide styling for webpage. Scripted index.js to allow interaction for the management of Solidity contracts.

Created deploy.py to deploy contracts, to load account, and to sources files. 
 
Established server.py to handle rest call that connects directly to our deployer.py and can execute the actions directly, while having the functionality of an actual webpage environment.

## Technologies
* Python 
* Pandas
* Solidity
* Streamlit
* web3
* MetaMask
* Ganache


## Outline
### High-Level: NFT Staking System
1.  An ERC721 will be the NFT token [1], used to identify owner.
2.  An ERC20 token will be the reward token.
3.	The eventsafe contract [2] will add extra security and keep track of tokens created.
4.  The staking contract[4] will hold the staked nft and will allow claiming the rewards.
5.	The reward, RSVPEvent contract [3] will be where the front end pulls from for admins

## Installation Instructions
To test on remix you need to compile and deploy the nft, reward token, and event owner address and input those parameters to create an RSVP event.  From there input whatever other variables needed for the function you want to accomplish.

## Usage 
Concerts, casinos, digital assets; any venue that could benefit from a secure incentivized attendence system that you can think of.

## Future Potential (& WIP)
Currently this has very exciting future potentials, especially in the post-Covid landscape.  There's a lot that can be added to this such as hosting it on a server that connects directly to our deployer.py and can execute the actions directly, while having the functionality of an actual webpage environment.  The folder "HTML server WIP" has a lot of the HTML that we worked on, but unfortunately ran into issues integrating with solcx.  This is the part that I believe warrants revisiting this project at a later date.

## App Video


https://user-images.githubusercontent.com/97809855/181617159-2313cc74-18b3-448c-8ed8-8e31c91c67b3.mov









## Reference
Acknowledge to the source of the original code for below four solidity contracts files.

## CITATION
    
### 1 - Nft721ME.sol
    
    Nakglom,Saravut (2022 , February 6) Github. solidity-avalanche-RSVP-staking-event/contracts/CreatorERC721.sol 
    https://github.com/SRVng/solidity-avalanche-RSVP-staking-event/blob/ec4c5ed57fc6edff239395e8b7dfa2b387e1bd82/contracts/CreatorERC721.sol

### 2 - eventSafeME.sol
    
    Nakglom,Saravut (2022 , February 6) Github. solidity-avalanche-RSVP-staking-event/contracts/EventSafe.sol 
    https://github.com/SRVng/solidity-avalanche-RSVP-staking-event/blob/main/contracts/EventSafe.sol

### 3 - rsvpEventME.sol
    
    Nakglom,Saravut (2022 , February 6) Github. solidity-avalanche-RSVP-staking-event/contracts/RSVP_Event.sol 
    https://github.com/SRVng/solidity-avalanche-RSVP-staking-event/blob/main/contracts/RSVP_Event.sol

### 4 - stakingME.sol
    
    Nakglom,Saravut (2022 , February 7) Github. solidity-avalanche-RSVP-staking-event/contracts/Staking.sol 
    https://github.com/SRVng/solidity-avalanche-RSVP-staking-event/blob/main/contracts/Staking.solS

## Contributors
| Name | GitHub | Linkedin | Email |
| ---- | ------ | -------- | ----- |
| Arthur Lovett | [ALovettII](https://github.com/ALovettII) | [LinkedIn](https://www.linkedin.com/in/arthurlovett/) | fintech@arthurlovett.com |
| Maureen Kaaria | [MaureenKC](https://github.com/MaureenKC) | [LinkedIn](https://www.linkedin.com/in/maureen-callahan/) | maureenkaaria@gmail.com |
| Khaing Thwe | [Khaingz](https://github.com/Khaingz) |    | khaingzt88@gmail.com | 
| Olga Koryachek | [Knyazhna](https://github.com/Knyazhna) | [LinkedIn](https://www.linkedin.com/in/olga-koryachek-a74b1877/?msgOverlay=true) | olgakoryachek@live.com | 
| Marco Bertone | [marcoberton](https://github.com/marcoberton) | marc.obertone@outlook.com  |

