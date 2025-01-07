import createEmployeesObject from './111-createEmployeesObject.js';
import createReportObject from './112-createReportObject.js';
const employees = {
  ...createEmployeesObject('engineering', ['Bob', 'Jane']),
  ...createEmployeesObject('marketing', ['Sylvie'])
};

