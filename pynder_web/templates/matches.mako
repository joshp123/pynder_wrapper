<%inherit file="pynder_web:templates/base.mako" />

<div class="page-header">
    <h1>Matches</h1>
</div>

% for match in matches:
    <div id=${match.id} class="match">
        <h3>
            <a href="${'/match/{}/messages/'.format(match.id)}">
            ${match.user.name} - ${match.user.age}
            </a>
        </h3>
        <p>${match.user.bio}</p>
        <div class="row images">
            % for image in match.user.photos:
                <div class="col-xs-6 col-md-3">
                    <div class="thumbanil">
                        <img class="thumbnail user" width=180 src=${str(image)}>
                    </div>
                </div>
            % endfor
        </div>
    </div>
% endfor
