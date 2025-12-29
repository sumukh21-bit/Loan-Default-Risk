import { useState } from "react";
function Component() {
    const [loanAmount, setLoanAmount] = useState("");
    const [loanTerm, setLoanTerm] = useState("");
    const [interest, setInterest] = useState("");
    const [income, setIncome] = useState("");
    const [employment, setEmployment] = useState("");
    const [homeOwnership, setHomeOwnership] = useState("");
    const [dti, setDti] = useState("");
    const [grade, setGrade] = useState("");
    const [result, setResult] = useState(null);
 

    const getPredict = async () => {
       
      const payload = {
      loan_amnt: Number(loanAmount),
      term: Number(loanTerm),
      int_rate: Number(interest),
      installment: Number(loanAmount) / Number(loanTerm || 1),
     
      annual_inc: Number(income),
      verification_status: 1,
      dti: Number(dti),
      delinq_2yrs: 0,
      emp_length: 6,
      inq_last_6mths: 0,
      open_acc: 5,
      pub_rec: 0,
      revol_bal: 2000,
      revol_util: 30,
      total_acc: 10,
      grade: grade,
      home_ownership: homeOwnership
    };

    

    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    setResult(data);
  };
    return (
        <header>
            <div className="All-Container">
                <h1 className="title">Loan Defaulter Application</h1>
            <div className="L-cont">
            <h3>Loan Details</h3>
                 
            <input type="number"  className="INPUT_field" placeholder="Loan Amount" id="LA" onChange={e => setLoanAmount(e.target.value)}></input>
            <input type="number"  className="INPUT_field" placeholder="Loan Term" id="LT" onChange={e => setLoanTerm(e.target.value)}></input>
            <input type="number"  className="INPUT_field" placeholder="Loan Intrest" id="LI" onChange={e => setInterest(e.target.value)}></input>

            </div>


            <div className="b-cont">
                <h3>Borrowers Profile</h3>
                <input type="number" className="INPUT_field" placeholder="Annual Income" onChange={e => setIncome(e.target.value)}></input>
            
              
              <input type="number" className="INPUT_field" placeholder="Debt to Income"onChange={e => setDti(e.target.value)}></input>
        

            </div>

            <div className="G-cont">
                <h3>Credit </h3>
                 <select onChange={e => setGrade(e.target.value)}>
                <option value="">Select Grade</option>
                {["A","B","C","D","E","F","G"].map(g => (
                    <option key={g} value={g}>{g}</option>
                ))}
                </select>
                <select onChange={e => setHomeOwnership(e.target.value)}>
                <option value="">Home Ownership</option>
                <option value="RENT">RENT</option>
                <option value="OWN">OWN</option>
                <option value="MORTGAGE">MORTGAGE</option>
                </select>

            
            <button onClick={getPredict}>Predict Default Risk</button>

            </div>
            

           
        </div>
            
            
       
        {result && (
        <div className="Result-Container">
          <h2>Result</h2>
          <p>Risk: <b>{result.risk}</b></p>
          <p>Risk to default: {(result.default_probability * 100).toFixed(2)}%</p>
        </div>
      )}
    </header>
       

  
    );
 
}





export default Component