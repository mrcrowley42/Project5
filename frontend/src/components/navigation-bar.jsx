export default function NavBar(){


    return (
    
        <div className="navigation">
        <a href="/">
            <button className="nav-title">WOE</button>
        </a>
        <a href="/admin">
            <button>Admin</button>
        </a>
        <a href="/dev">
            <button>Dev</button>
        </a>
        <a href="/user">
            <button>User</button>
        </a>
        <a href="/other">
            <button>Other</button>
        </a>
    </div>

    
    );
}