% rebase('layout.tpl', title=title, stylesheet=stylesheet, visits=visits, unique=unique)

<h1>Посещения</h1>
<p>(GMT+05:00 Екатеринбург)</p>
<table>
    %for entry in visitsTable:
    %ip = entry[1]
    %time = entry[0]
    % browser = entry[2]
    <tr>
        <td>{{ip}}</td>
        <td>{{time}}</td>
        <td>{{browser}}</td>
    </tr>
    %end
</table>