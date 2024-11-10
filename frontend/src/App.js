import React, { useState, useEffect } from 'react';
import StudentList from './components/StudentList';
import StudentForm from './components/StudentForm';

function App() {
  // Initialize students as an empty array
  const [students, setStudents] = useState([]);

  // Fetch students from the API
  useEffect(() => {
    fetch('http://localhost:5000/students')
      .then((response) => response.json())
      .then((data) => {
        // Ensure data is an array before setting it
        if (Array.isArray(data)) {
          setStudents(data);
        } else {
          console.warn('Data from API is not an array', data);
          setStudents([]); // Set to empty array if data is not an array
        }
      })
      .catch((error) => {
        console.error('Error fetching students:', error);
        setStudents([]); // Set to empty array if there’s an error
      });
  }, []); // Empty dependency array to run only once on mount

  // Render the StudentList component and pass students as a prop
  return (
    <div className="App">
      <h1>Student Management</h1>
      <StudentForm />
      
      {/* Conditionally render StudentList only if students is an array */}
      {Array.isArray(students) && students.length > 0 ? (
        <StudentList students={students} />
      ) : (
        <p>No students available.</p>
      )}
    </div>
  );
}

export default App;
