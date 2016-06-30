<%inherit file="pynder_web:templates/base.mako" />

<div class="page-header">
    <h1>Matches: ${len(matches)}</h1>
</div>

<div class="row matches">
    % for match in matches:
        <%
        from pynder_core.tinder import humanized_delta
        her_count = len([m for m in match.messages if m.sender.id == match.user.id])
        me_count = len(match.messages) - her_count
        if len(match.messages):
            last = humanized_delta(match.messages[-1].sent)
            if match.messages[-1].sender.id == match.user.id:
                last += " (her)"
            else:
                last += " (me)"
        else:
            last = "Never messaged"
        %>

        <div id=${match.id} class="col-md-4">
            <div class="card match">
                <div class="card-block">
                    <h4 class="card-title">
                        <a href="${'/match/{}/messages/'.format(match.id)}">
                        ${match.user.name} - ${match.user.age}
                        </a>
                    </h4>
                </div>
                <small class="text-muted">
                    her: ${her_count} me: ${me_count}
                    <br>
                    last: ${last}
                </small>
                <p>${"<br />".join(match.user.bio.split('\n'))}</p>
                <div class="row images">
                    % for image in match.user.photos:
                        <div class="col-xs-6">
                            <img class="img-fluid img-thumbnail user"
                                 notsrc="http://placehold.it/600x600"
                                 src=${str(image)}>
                        </div>
                    % endfor
                </div>
            </div>
        </div>
    % endfor
</div>
