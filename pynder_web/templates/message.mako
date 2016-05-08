<%inherit file="pynder_web:templates/base.mako" />


<!-- TODO: add match as a template and import the match here at the top of the page -->

<%
from pynder_core.tinder import humanized_delta
from pynder_web import session
%>

<table class='table table-hover messages' id="${match.id}">
    <tr>
        <th>Name</th>
        <th>Time</th>
        <th>Message</th>
    </tr>
    % for message in messages:
        % if message.sender.id != session.session.profile.id:
            <tr class=table-info>
        % else:
            <tr>
        % endif
            <td>${str(message.sender.name)}</td>
            <td>${humanized_delta(message.sent)}</td>
            <td>${message.body}</td>
        </tr>
    % endfor
</table>
