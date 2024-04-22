export default function NavBar(){


    return (
    
        <div className="navigation">
        {/* <a href="{% url 'index' %}"> */}
            <button class="nav-title">WOE</button>
        {/* </a> */}
        {/* <a href="{% url 'admin' %}"> */}
            <button>Admin</button>
        {/* </a> */}
        {/* <a href="{% url 'dev_page' %}"> */}
            <button>Dev</button>
        {/* </a> */}
        {/* <a href="{% url 'user_page' %}"> */}
            <button>User</button>
        {/* </a> */}
    </div>

    
    );
}