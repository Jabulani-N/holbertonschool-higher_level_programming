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

## Task2,3

`require('process').argv` returns an array: `[javascript location (shebang), called function/file, user arguments]`. make a `const` equal to it to clenaly make use of it.

* `"this will be counted as a single agument because of the quotes"`

## Task4

```

const str1 = "example string"

const str2 = str1.concat('example of string', 'to tag onto' the guy before the dot.')

```

* string is immutable, so note that this returns a new string to str2, without altering str1

## Task5

[NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN) is a property that means "not a number". `isNaN(varibale)` will tell you if varaible is a _not_ a number. it will parseint first, as necessary.

[parseint(varibale)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) converts `variable` into it's int equivalent if possible, such as turning `"89"` into `89`.

```

if (isNaN(variableInQuestion)) {

    //do stuff here

}

```

## Task9

```
function functionName (arg1, arg2, ...) {
  // do stuff
}
```

you can put this in your script, and then call `functionName` from anywhere
