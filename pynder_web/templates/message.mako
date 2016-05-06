<!-- TODO: add match as a template and import the match here at the top of the page -->

<%
from pynder_core.tinder import humanized_delta
%>

<table class='messages' id="${match.id}">
    <th>
        <td>Name</td>
        <td>Time</td>
        <td>Message<td>
    </th>
    % for message in messages:
        <tr>
            <td>${str(message.sender.name)}</td>
            <td>${humanized_delta(message.sent)}</td>
            <td>${message.body}</td>
        </tr>
    % endfor
</table>
