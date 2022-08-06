function hide_all() {
    var entries = document.getElementsByClassName('entry');
    for (var i=0; i < entries.length; i++) {
        entries[i].classList.add('hidden_entry');
    }
}

function show_entries_w_tag(tag) {
    var entries = document.getElementsByClassName(tag);
    for (var i=0; i < entries.length; i++) {
        entries[i].classList.remove('hidden_entry');
    }
}

function tag_to_param(tag) {
    return tag.trim().replace(/ /g, "_").replace(/\./g, '-').replace(/[^a-zA-Z0-9_\-]/g, '');
}

function convert_tag_links() {
    var entries = document.getElementsByClassName('tag_link');
    for (var i=0; i < entries.length; i++) {
        entries[i].href = "/blog/?tag=" + tag_to_param(entries[i].innerText);
    }
}

function fill_month(month_num) {
    var months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December'];
    document.getElementById('month_name').innerHTML = months[parseInt(month_num)];
}

function filter_tags() {
    hide_all();
    var url = window.location.href;
    if (url.search('tag') === -1) {
        show_entries_w_tag("entry");
        return;
    }

    // Get the title tag (<h1>) so we can change it after we gather the tags
    var title_tag = document.getElementById('blog-index').getElementsByTagName('h1')[0];
    var new_title = 'Entries with tag: ';

    var queries = url.split('?')[1].split('#')[0];  // Get everything after ? and before #
    queries = queries.split('&');
    var q_val, q_type;

    // Gather the tags, show each one, add them to the new title
    for (var i=0; i < queries.length; i++) {
        [q_type, q_val] = queries[i].split('=');
        if (q_type !== 'tag') continue;
        show_entries_w_tag(q_val);
        new_title += q_val + ' ';
    }

    // Change the title of the page
    title_tag.innerHTML = new_title;
}
