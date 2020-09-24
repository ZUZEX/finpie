// https://stackoverflow.com/questions/50573455/modifying-the-javascript-navigator-object-with-selenium
const setProperty = () => {
    Object.defineProperty(navigator, "languages", {
        get: function() {
            return ["en-US", "en", "es"];
        }
    });

    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5],
    });

    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined,
    });
    callback();
};
setProperty();
