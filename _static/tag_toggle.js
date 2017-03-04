function hide_all() {
    var entries = document.getElementsByClassName('entry');
    for (i=0; i < entries.length; i++) {
        entries[i].classList.add('hidden_entry');
    }
}

function show_entries_w_tag(tag) {
    var entries = document.getElementsByClassName(tag);
    for (i=0; i < entries.length; i++) {
        entries[i].classList.remove('hidden_entry');
    }
}

function tag_to_param(tag) {
    return tag.trim().replace(/ /g, "_").replace(/\./g, '-').replace(/[^a-zA-Z0-9_\-]/g, '');
}

function convert_tag_links() {
    var entries = document.getElementsByClassName('tag_link');
    for (i=0; i < entries.length; i++) {
        entries[i].href = "/blog/?tag=" + tag_to_param(entries[i].innerText);
    }
}

function fill_month(month_num) {
    var months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December'];
    document.getElementById('month_name').innerHTML = months[parseInt(month_num)];
}
