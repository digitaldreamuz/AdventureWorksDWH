CREATE TABLE JobCandidate (
    JobCandidateID SERIAL PRIMARY KEY,
    BusinessEntityID INT REFERENCES Employee(BusinessEntityID),
    Resume XML, -- PostgreSQL supports XML type
    ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
