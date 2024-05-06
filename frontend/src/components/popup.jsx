export default function PopUp(props) {
    window.onclick = function(event) {
        if (event.target == this.window) {
            this.show = false;
        }
    }
    return (

        props.show ? (<div className="modal" id="myModal" style={{ display: "block" }}>
            <div className="modal-content">
                <span onClick={props.close} className="close">&times;</span>
                {props.content}
            </div>
        </div>

        ) : <></>)
}