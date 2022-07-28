const baseDomain = 'https://127.0.0.1:8000';

let responseElement;
let responseTextElement;

let createRsvpRewardElement;
let createRsvpNFTElement;
let createRsvpOwnerElement;

window.addEventListener('DOMContentLoaded', (event) => {
    responseElement = document.querySelector('#response');
    responseTextElement = document.querySelector('#responseText');

    createRsvpRewardElement = document.querySelector('#createRsvpReward');
    createRsvpNFTElement = document.querySelector('#createRsvpNFT');
    createRsvpOwnerElement = document.querySelector('#createRsvpOwner');
});

function request(action) {
    let url = `${baseDomain}?action=${action}`;

    if (action === 'create_rsvp') {
        url += `&reward=${createRsvpRewardElement.value}`;
        url += `&nft=${createRsvpNFTElement.value}`;
        url += `&owner=${createRsvpOwnerElement.value}`;
    }
    // fetch(url).then((response)=>{
    responseTextElement.innerHTML = url;
    // responseTextElement.innerHTML = response;
    // });
}