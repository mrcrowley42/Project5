export default function PopUp(props) {
    return (

        props.show ? (<div className="modal" id="myModal" style={{ display: "block" }}>
            <div className="modal-content">
                <span onClick={props.close} className="close">&times;</span>
                {props.content}
                <p> where is the window?</p>
            </div>
        </div>

        ) : <></>)
}