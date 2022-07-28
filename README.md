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
1.  An ERC721 will be the NFT (RSVP) token, used to identify owner.
2.  An ERC20 token will be the reward token.
3.	The eventsafe contract will add extra security and keep track of tokens created.
4.  The staking contract will hold the staked nft and will allow claiming the rewards.
5.	The reward RSVP contract will be where the front end pulls from for admins

## Installation Instructions
To test on remix you need to compile and deploy the nft, reward token, and event owner address and input those parameters to create an RSVP event.  From there input whatever other variables needed for the function you want to accomplish.

## Usage 
Concerts, casinos, digital assets; any venue that could benefit from a secure incentivized attendence system that you can think of.

## Future Potential (& WIP)
Currently this has very exciting future potentials, especially in the post-Covid landscape.  There's a lot that can be added to this such as hosting it on a server that connects directly to our deployer.py and can execute the actions directly, while having the functionality of an actual webpage environment.  The folder "HTML server WIP" has a lot of the HTML that we worked on, but unfortunately ran into issues integrating with solcx.  This is the part that I believe warrants revisiting this project at a later date.

## App Video


https://user-images.githubusercontent.com/97809855/181617159-2313cc74-18b3-448c-8ed8-8e31c91c67b3.mov




## Contributors
| Name | GitHub | Linkedin | Email |
| ---- | ------ | -------- | ----- |
| Arthur Lovett | [ALovettII](https://github.com/ALovettII) | [LinkedIn](https://www.linkedin.com/in/arthurlovett/) | fintech@arthurlovett.com |
| Maureen Kaaria | [MaureenKC](https://github.com/MaureenKC) | [LinkedIn](https://www.linkedin.com/in/maureen-callahan/) | maureenkaaria@gmail.com |
| Khaing Thwe | [Khaingz](https://github.com/Khaingz) |    | khaingzt88@gmail.com | 
| Olga Koryachek | [Knyazhna](https://github.com/Knyazhna) | [LinkedIn](https://www.linkedin.com/in/olga-koryachek-a74b1877/?msgOverlay=true) | olgakoryachek@live.com | 
| Marco Bertone | [marcoberton](https://github.com/marcoberton) | marc.obertone@outlook.com  |

