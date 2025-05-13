// function createPhoneNumber(numbers) {
//     let phoneNumber = "(xxx) xxx-xxxx";
  
    for (let i = 0; i < numbers.length; i++) {
      phoneNumber = phoneNumber.replace('x', numbers[i]);
    }
  
    return phoneNumber;
  
  
  console.log(createPhoneNumber([0, 7, 2, 0, 9, 5, 3, 3, 3, 1])); // (072) 095-3331

  //jaden case
  function toJadenCase(str) {
    return str
      .split(' ')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  }
  
  // Test case
  console.log(toJadenCase("most trees are blue"));
  console.log(toJadenCase("how can mirrors be real if our eyes aren't real"));

  //functional phone number
  function generatePhoneNumber() {
    // Generate a random 10-digit number
    const areaCode = Math.floor(Math.random() * 900 + 100); // Ensures a 3-digit area code between 100 and 999
    const centralOfficeCode = Math.floor(Math.random() * 900 + 100); // Same logic for the next 3 digits
    const lineNumber = Math.floor(Math.random() * 10000 + 1000); // Ensures 4 digits
  
    // Format the phone number
    return `(${areaCode}) ${centralOfficeCode}-${lineNumber}`;
  }
  
  // Example usage:
  console.log(generatePhoneNumber());
  // Output: "(123) 456-7890" (the actual numbers will vary due to randomization)
  