CREATE TABLE employee (
    BusinessEntityID     INTEGER PRIMARY KEY,
    NationalIDNumber     VARCHAR(15) NOT NULL,
    LoginID              VARCHAR(256) NOT NULL,
    OrganizationNode     TEXT,  -- Converted from hierarchyid
    OrganizationLevel    SMALLINT,
    JobTitle             VARCHAR(50) NOT NULL,
    BirthDate            DATE NOT NULL,
    MaritalStatus        CHAR(1) NOT NULL,
    Gender               CHAR(1) NOT NULL,
    HireDate             DATE NOT NULL,
    SalariedFlag         BOOLEAN NOT NULL,
    VacationHours        SMALLINT NOT NULL,
    SickLeaveHours       SMALLINT NOT NULL,
    CurrentFlag          BOOLEAN NOT NULL,
    rowguid              UUID NOT NULL,  -- Converted from uniqueidentifier
    ModifiedDate         TIMESTAMP NOT NULL
);
