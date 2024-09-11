
var nome = prompt("Por favor digite  o seu nome:");

var alturaCm = parseFloat(prompt("Por Favor digite sua altura em centímetros:"));

var peso = parseFloat(prompt("Por Favor digite seu peso em kg:"));


var alturaM = alturaCm / 100;

///////////////// Calcula o IMC /////////////////


var imc = peso / (alturaM * alturaM);

///////////////// Classifica o IMC /////////////////


var classificacao;
if (imc < 16) {
    classificacao = "Baixo peso, muito grave";
} else if (imc >= 16 && imc <= 16.99) {
    classificacao = "Baixo peso, grave";
} else if (imc >= 17 && imc <= 18.49) {
    classificacao = "Baixo peso";
} else if (imc >= 18.50 && imc <= 24.99) {
    classificacao = "Peso normal";
} else if (imc >= 25 && imc <= 29.99) {
    classificacao = "Sobrepeso";
} else if (imc >= 30 && imc <= 34.99) {
    classificacao = "Obesidade grau I";
} else if (imc >= 35 && imc <= 39.99) {
    classificacao = "Obesidade grau II";
} else {
    classificacao = "Obesidade grau III";
}

////////////// Exibir o Resultado ////////////////



alert("Nome: " + nome + "\nIMC: " + imc + "\nClassificação: " + classificacao);
