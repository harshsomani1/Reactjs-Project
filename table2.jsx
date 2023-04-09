import React, { useState } from 'react'
import BarGraph from "./ess"
import data from "./chembl.json"
import api_response_as_json from './test.py'
function Tableau(){
    
    const [entries, setContacts] = useState(data);
    
    return(<>
    <input type="text" id='script' name="scriptbutton"  ></input><table align='center' id="customers">
        
        <thead>
            <th>ChemblID</th>
            <th>Toxicity Class</th>
            
        </thead>
        <tbody>
            {entries.map((contact)=>(
                <tr>
                    <td>{contact['id']}</td>
                    <td>{contact.toxscore}</td>
                 </tr>
            ))}
            <tr></tr>
        </tbody>
    
    </table>
   </>
    )   
}
export default Tableau;