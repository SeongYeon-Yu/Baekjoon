const readline = require('readline'); //입력받을 때 readline

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on('line', function (line) {
    const input = line.split(' '); // 입력 값 띄어쓰기로 구분

    const a = Number(input[0]); //첫번째 값 a
    const b = Number(input[1]); // 두번째 값 b

    if (a > b) {
        console.log('>');
    } else if (a < b) {
        console.log('<');
    } else {
        console.log('==');
    }

    rl.close();
}).on('close', function () {
    process.exit();
});