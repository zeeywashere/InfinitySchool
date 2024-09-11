
var numeroDeEstudantes = parseInt(prompt("Por Favor, digite o número total de estudantes na turma:"), 10);


var somaNotas = 0;
var maiorNota = -Infinity;
var menorNota = Infinity;


for (var i = 1; i <= numeroDeEstudantes; i++) {
    
    var nota = parseFloat(prompt("Digite a nota do estudante " + i + ":"));

    somaNotas += nota;

    if (nota > maiorNota) maiorNota = nota;
    if (nota < menorNota) menorNota = nota;
}

/////////////// Calcula a média ///////////////


var media = somaNotas / numeroDeEstudantes;

/////////////// Mostra o resultado ///////////////

console.log("Média da turma: " + media);
console.log("Maior nota: " + maiorNota);
console.log("Menor nota: " + menorNota);
