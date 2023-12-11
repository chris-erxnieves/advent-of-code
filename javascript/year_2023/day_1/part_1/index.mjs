import { readFileSync } from 'fs';
import { dirname } from 'path';

const processFile = (fileName) => {
    const path = new URL(dirname(import.meta.url) + `/${fileName}`).pathname;
    return readFileSync(path).toString().split(/\r?\n/).filter(Boolean);
};

const getCalibrationValue = (str) => {
    const { first, last } = str.split('').reduce((acc, val) => {
        if (!isNaN(parseInt(val, 10))) {
            if (acc.first === '') acc.first = val;
            acc.last = val;
        }

        return acc;
    }, { first: '', last: '' });
    return parseInt(first + last, 10);
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