import React, { useState, useEffect } from "react";
import axios from 'axios';
import PopUp from "../components/popup"



export default function Admin() {


  function manualIngest() {


    alert('Ingesting data...')
  }

  function addEntry() {
    setVisible(true);


  }

  function Content() {

    return (
      <>
        <form action="http://127.0.0.1:8000/admin/" className="test" encType="multipart/form-data" method="post" name="hi">

          <table className="editableTable" id="editSourceTable">
            <thead>
              <tr>
                <th className="idColumn">ID</th>
                <th>Name</th>
                <th>WMO_id</th>
                <th>URL</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="idColumn"><input id="new_id" name="id" defaultValue={sources[stuff].id} /></td>
                <td><input id="new_name" name="name" defaultValue={sources[stuff].name} /></td>
                <td><input id="new_wmo" name="wmo_id" defaultValue={sources[stuff].wmo_id} /></td>
                <td><input id="new_url" name="url" defaultValue={sources[stuff].url} /></td>
              </tr>
            </tbody>
          </table>
          <button className="submitButton" type="submit">Update</button>
        </form>
      </>
    )
  }

  function editEntry(e, id) {
    setVisible(true);
    var value = e.target.closest('tr').rowIndex - 1;
    setStuff(value);

  }

  function deleteEntry(e, id) {
    var value = e.target.closest('tr').rowIndex - 1;
    var sourceId = sources[value].id;
    console.log(sourceId);
    // if (confirm("Are you sure you want to delete this entry?")){
    //   console.log("yes");
    // }
    var request = new XMLHttpRequest();

    // https://www.youtube.com/watch?v=k6ELzQgPHMM

    // request.ready
    // url = "{% url 'delete_source' %}" ;
    // request.open("POST", url) ;
    // var CSRF_TOKEN = '{{ csrf_token }}';
    // request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    // request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // request.send("id=" + source_id);

  }

  const [visible, setVisible] = useState(false)

  function openModal() {
    setVisible(true);
  }
  function closeModal() {
    setVisible(false);
  }

  const [sources, setSources] = useState([])
  const [stuff, setStuff] = useState(0)
  const [loading, setLoading] = useState(false)
  useEffect(() => {
    setLoading(true)
    axios.get("http://127.0.0.1:8000/api/admins/")
      .then(response => response.data)
      .then(json => {
        setSources(json);
      })
      .finally(() => {
        setLoading(false)
      })
  }, [])




  return (
    <>
      {loading ?
        (<div>Loading...</div>)
        : (

          <>
            <h1>Admin Page</h1>
            <h2>Sources table</h2>
            <table className="sourceTable">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>WMO id</th>
                  <th>URL</th>
                </tr>
              </thead>
              <tbody>
                {sources.map(obs => (


                  <tr key={obs.id}>
                    <td>{obs.name}</td>
                    <td>{obs.wmo_id}</td>
                    <td>{obs.url}</td>

                    <td className="editRow" onClick={(e) => {
                      editEntry(e, 1);
                    }} title="Edit">
                      <svg className="icon" fill="currentColor" height="16" viewBox="0 0 16 16" width="16"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325" />
                      </svg>
                    </td>
                    <td className="editRow"
                      onClick={(e) => {
                        deleteEntry(e, 1);
                      }}
                      title="Remove">
                      <svg className="icon" height="16" viewBox="0 0 16 16" width="16"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                        <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                      </svg>
                    </td>

                  </tr>
                ))}</tbody>
            </table>
          </>

        )
      }

      <button className="submitButton" onClick={(e) => { addEntry(e); }}>Add Source +</button>
      <> </>
      <button className="submitButton" onClick={manualIngest} title="Click to ingest new data from sources" type="button">Do
        Manual Ingest
      </button>


      <> </>
      <button className="submitButton" title="Click to Reload the Webserver" type="button">Reload
        Server
      </button>

      <PopUp show={visible} close={closeModal} content={<Content />} />
    </>
  )



}