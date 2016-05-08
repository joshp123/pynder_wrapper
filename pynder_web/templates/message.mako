<%inherit file="pynder_web:templates/base.mako" />


<!-- TODO: add match as a template and import the match here at the top of the page -->

<%
from pynder_core.tinder import humanized_delta
from pynder_web import session
%>

<table class='table table-sm table-hover messages' id="${match.id}">
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
            <td nowrap>${humanized_delta(message.sent)}</td>
            <td>${message.body}</td>
        </tr>
    % endfor
</table>

<form id="messagebox">
    <div class="form-group row" style="margin-bottom: 0">
        <label class="col-xs-1" for="replyToMessage">Reply:</label>
    </div>
    <div class="form-group row">
        <div class="col-sm-10">
            <textarea class="form-control col-xs-9" name="message" id="reply" form="messagebox" placeholder="..."></textarea>
        </div>
        <div class="col-sm-2">
          <button type="submit" class="btn btn-primary">Send</button>
        </div>
    </div>
</form>

<script type="text/javascript">
    $(document).scrollTop($(document).height());
    $(function() {
        $('#messagebox').submit(function() {
            message = $('#reply').val();
            $.ajax({
                type: 'POST',
                url: '../message/',
                data: JSON.stringify({'message': message}),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function() {
                    window.location.reload();
                    // TODO: maybe refresh the session? 
                }
            });
            return false;
        });
    })
</script>
