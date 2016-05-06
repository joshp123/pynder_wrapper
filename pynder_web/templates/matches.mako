<h1>Matches</h1>

% for match in matches:
    <div id=${match.id} class="match">
        <h3>
            <a href="${'/match/{}/messages/'.format(match.id)}">
            ${match.user.name} - ${match.user.age}
            </a>
        </h3>
        <p>${match.user.bio}</p>
        <div class="images">
            % for image in match.user.photos:
                <img class="user" width=100" src=${str(image)}>
            % endfor
        </div>
    </div>
% endfor
