CREATE TABLE Shift (
    ShiftID SMALLINT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    ModifiedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
