CREATE TABLE EmployeeDepartmentHistory (
    BusinessEntityID INT REFERENCES Employee(BusinessEntityID),
    DepartmentID SMALLINT REFERENCES Department(DepartmentID),
    ShiftID SMALLINT REFERENCES Shift(ShiftID),
    StartDate DATE NOT NULL,
    EndDate DATE,
    ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (BusinessEntityID, DepartmentID, ShiftID, StartDate)
);
