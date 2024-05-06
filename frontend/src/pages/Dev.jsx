import PopUp from "../components/popup"
import React, { useState, useEffect } from "react";
import axios from 'axios';



export default function Dev() {

  
  const [visible, setVisible] = useState(false);
  const [logData, loadLog] = useState("");

  function openModal() {
    setVisible(true);
    axios.get("http://127.0.0.1:8000//load_log")
      .then(response => response.data)
      .then(json => {
        loadLog(json)})
    
    
  }
  function closeModal() {
    setVisible(false);
  }

  function Content() {

    return (
      <>
        <textarea id="logContent" value={logData} readOnly style={{ resize: "none", scroll: "auto", width: "100%", height: "50vh" }} ></textarea>
      </>
    )
  }

  return (
    <>
      <h1>Developer Page</h1>
      <form className="fileUpload" encType="multipart/form-data" method="post">

        <input multiple name="document" type="file"></input>
        <>  </>
        <button type="submit">Upload Json</button>
      </form>

      <button className="submitButton" onClick={openModal} type="button">View Log</button>
      <PopUp show={visible} close={closeModal} content={<Content />} />
    </>
  )

}