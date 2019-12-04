/**
 * Dependency Modules
 */
var assert = require("assert").strict;
var webdriver = require("selenium-webdriver");
var chrome = require('selenium-webdriver/chrome');
var path = require('chromedriver').path;
require("geckodriver");// Application Server
const serverUri = "http://localhost:3000/#";
const appTitle = "React Selenium App";

/**
 * Config for Chrome browser
 * @type {webdriver}
 */
var service = new chrome.ServiceBuilder(path).build();
chrome.setDefaultService(service);
var browser = new webdriver.Builder()
 .usingServer()
 .withCapabilities(webdriver.Capabilities.chrome())
 .build();
 
 /**
 * Function to get the title and resolve it it promise.
 * @return {[type]} [description]
 */
function logTitle() {
 return new Promise((resolve, reject) => {
  browser.getTitle().then(function(title) {
   resolve(title);
  });
 });
}

/**
 * Sample test case
 * To check whether the given value is present in array.
 */
describe("Array", function() {
 describe("#indexOf()", function() {
  it("should return -1 when the value is not present", function() {
   assert.equal([1, 2, 3].indexOf(4), -1);
  });
 });
});describe("Home Page", function() {
 
 /**
  * Test case to load our application and check the title from index.html file
  */
 it("Should load the home page and get title", function() {
  this.timeout(15000);
  return new Promise((resolve, reject) => {
   browser
    .get(serverUri)
    .then(logTitle)
    .then(title => {
     assert.strictEqual(title, appTitle);
     resolve();
    })
    .catch(err => reject(err));
  });
 });
 
 /**
  * Test case to check whether the login button is loaded.
  */
 it("Should check whether the given element is loaded", function() {
  this.timeout(15000);
  return new Promise((resolve, reject) => {
   browser
    .findElement({ id: "login" })
    .then(elem => resolve())
    .catch(err => reject(err));
  });
 });
 
 /**
  * End of test cases use.
  * Closing the browser and exit.
  */
 after(function() {
  // End of test use this.
  browser.quit();
 });
});