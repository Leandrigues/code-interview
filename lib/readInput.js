module.exports = function readInput(func) {
    const readline = require('readline');
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
      terminal: false
    });
    rl.on('line', function(line){
      console.log(func(line))
      rl.close()
    })
  }
