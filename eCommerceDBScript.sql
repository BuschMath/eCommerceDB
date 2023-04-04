alter table departments alter column departmentHeads int;

alter table departments add constraint deptHead_fk_employee 
	foreign key  (departmentHeads) references employee(employeeID);