CREATE TABLE EmployeePayHistory (
    BusinessEntityID INT REFERENCES Employee(BusinessEntityID),
    RateChangeDate TIMESTAMP NOT NULL,
    Rate NUMERIC(19,4) NOT NULL, -- `money` in SQL Server maps to `NUMERIC(19,4)`
    PayFrequency SMALLINT NOT NULL,
    ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (BusinessEntityID, RateChangeDate)
);
