import React, { useState } from 'react';

function StudentForm() {
  const [formData, setFormData] = useState({
    std_name: '',
    std_email: '',
    std_address: '',
    std_phone: '',
    std_class: '',
    std_subject: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/students/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        console.error('Failed to create student:', response.statusText);
      } else {
        console.log('Student created successfully');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="std_name" placeholder="Name" onChange={handleChange} />
      <input type="email" name="std_email" placeholder="Email" onChange={handleChange} />
      <input type="text" name="std_address" placeholder="Address" onChange={handleChange} />
      <input type="text" name="std_phone" placeholder="Phone" onChange={handleChange} />
      <input type="text" name="std_class" placeholder="Class" onChange={handleChange} />
      <input type="text" name="std_subject" placeholder="Subject" onChange={handleChange} />
      <button type="submit">Create Student</button>
    </form>
  );
}

export default StudentForm;
