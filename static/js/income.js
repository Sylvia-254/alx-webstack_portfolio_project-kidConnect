import getFullBudgetObject from 'getFullBudget.js';
const fullBudget = getFullBudgetObject(20, 50, 10);
console.log(fullBudget.getIncomeInDollars(fullBudget.income));
console.log(fullBudget.getIncomeInEuros(fullBudget.income));

