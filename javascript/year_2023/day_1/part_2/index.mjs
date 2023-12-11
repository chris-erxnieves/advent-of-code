import { readFileSync } from 'fs';
import { dirname } from 'path';

const NumbersEnum = Object.freeze({
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
});

const processFile = (fileName) => {
    const path = new URL(dirname(import.meta.url) + `/${fileName}`).pathname;
    return readFileSync(path).toString().split(/\r?\n/).filter(Boolean);
};

const getCalibrationValue = (str) => {
    const { first, last } = str.split('').reduce((acc, val, i) => {
        if (isNaN(parseInt(val, 10))) {
            const substr = str.slice(0, i + 1);
            const found  = Object.entries(NumbersEnum).find(([key]) => substr.endsWith(key));
            if (found) {
                if (acc.first === '') acc.first = found[1];
                acc.last = found[1];
            }
        } else {
            if (acc.first === '') acc.first = val;
            acc.last = val;
        }

        return acc;
    }, { first: '', last: '' });
    return parseInt(`${first}${last}`, 10);
};

const sumCalibrationValues = (fileName) =>
    processFile(fileName).reduce((acc, val) => {
        acc += getCalibrationValue(val);
        return acc;
    }, 0);

(() => {
    console.log('---Example---');
    console.log(sumCalibrationValues('example.txt'));

    console.log('---Input---');
    console.log(sumCalibrationValues('input.txt'));
})();