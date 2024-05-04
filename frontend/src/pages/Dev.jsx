import PopUp from "../components/popup"
import React, { useState, useEffect } from "react";


function Content() {

  return (
    <>
      <textarea id="logContent" readOnly style={{ resize: "none", scroll: "auto", width: "100%", height: "50vh" }} ></textarea>
    </>
  )
}

export default function Dev() {
  const [visible, setVisible] = useState(false)

  function openModal() {
    setVisible(true);
  }
  function closeModal() {
    setVisible(false);
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