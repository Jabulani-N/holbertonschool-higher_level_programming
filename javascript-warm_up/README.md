# JavaScript - Warm up

# Resources

* [![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)

* [Javascript Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)

## Install Node 14

```

$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

$ sudo apt-get install -y nodejs

```

## Install semi-standard

`$ sudo npm install semistandard --global`

[semistandard](https://www.npmjs.com/package/semistandard) is a linter with excellent functionality

* `semistandard fileName` will have seminstandard judge fileName for coding style.

* * it will give a lightly flavored review and sugest you use `semistandard --fix` instead.

* `semistandard --fix fileName` will fix fileName to align with relevant style. not specifying one will target everything withing the directory

## Task0

Testing: `./0-javascript_is_amazing.js`

* a successful test will pring the line “JavaScript is amazing”

## Task1

Testing: `./1-multi_languages.js`

* a successful test will pring 3 lines of text
