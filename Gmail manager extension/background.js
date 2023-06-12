// Listen for messages from the popup.js file
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "selectAndDelete") {
      selectAndDeleteEmails();
    } else if (request.action === "sortByCategory") {
      sortByCategory();
    } else if (request.action === "sortByDate") {
      sortByDate();
    } else if (request.action === "sortBySender") {
      sortBySender();
    } else if (request.action === "showSameSender") {
      showSameSender();
    }
  });
  
  // Function to select and delete emails
  function selectAndDeleteEmails() {
    chrome.tabs.query({ url: "https://mail.google.com/*" }, (tabs) => {
      if (tabs.length > 0) {
        chrome.tabs.executeScript(tabs[0].id, { file: "selectAndDelete.js" });
      }
    });
  }
  
  // Function to sort emails by category
  function sortByCategory() {
    chrome.tabs.query({ url: "https://mail.google.com/*" }, (tabs) => {
      if (tabs.length > 0) {
        chrome.tabs.executeScript(tabs[0].id, { file: "sortByCategory.js" });
      }
    });
  }
  
  // Function to sort emails by date
  function sortByDate() {
    chrome.tabs.query({ url: "https://mail.google.com/*" }, (tabs) => {
      if (tabs.length > 0) {
        chrome.tabs.executeScript(tabs[0].id, { file: "sortByDate.js" });
      }
    });
  }
  
  // Function to sort emails by sender
  function sortBySender() {
    chrome.tabs.query({ url: "https://mail.google.com/*" }, (tabs) => {
      if (tabs.length > 0) {
        chrome.tabs.executeScript(tabs[0].id, { file: "sortBySender.js" });
      }
    });
  }
  
  // Function to show emails from the same sender
  function showSameSender() {
    chrome.tabs.query({ url: "https://mail.google.com/*" }, (tabs) => {
      if (tabs.length > 0) {
        chrome.tabs.executeScript(tabs[0].id, { file: "showSameSender.js" });
      }
    });
  }
  