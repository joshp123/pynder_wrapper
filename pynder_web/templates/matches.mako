<%inherit file="pynder_web:templates/base.mako" />

<div class="page-header">
    <h1>Matches</h1>
</div>

<div class="row matches">
    % for match in matches:
        <div id=${match.id} class="col-md-4">
            <div class="card match">
                <div class="card-block">
                    <h4 class="card-title">
                        <a href="${'/match/{}/messages/'.format(match.id)}">
                        ${match.user.name} - ${match.user.age}
                        </a>
                    </h4>
                </div>
                <p>${match.user.bio}</p>
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
