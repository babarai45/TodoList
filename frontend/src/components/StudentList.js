import React from 'react';

function StudentList({ students }) {
  return (
    <div>
      <h2>Student List</h2>
      {students.map((student) => (
        <div key={student.id}>
          <p>Name: {student.std_name}</p>
          <p>Email: {student.std_email}</p>
          {/* Render other student details as needed */}
        </div>
      ))}
    </div>
  );
}

export default StudentList;
