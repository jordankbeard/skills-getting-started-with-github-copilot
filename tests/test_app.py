def test_get_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert expected_activity in data
    assert "participants" in data[expected_activity]


def test_signup_and_delete(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act: sign up
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert sign up succeeded
    assert signup_response.status_code == 200
    assert email in client.get("/activities").json()[activity_name]["participants"]

    # Act: unregister
    delete_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email}
    )

    # Assert unregister succeeded
    assert delete_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_root_redirect(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in {301, 307, 308}
    assert response.headers["location"] == expected_location
