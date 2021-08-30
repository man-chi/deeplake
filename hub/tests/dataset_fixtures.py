import pytest
import hub

enabled_datasets = pytest.mark.parametrize(
    "ds",
    ["memory_ds", "local_ds", "s3_ds", "gcs_ds"],
    indirect=True,
)

enabled_non_gcs_datasets = pytest.mark.parametrize(
    "ds",
    ["memory_ds", "local_ds", "s3_ds"],
    indirect=True,
)

enabled_persistent_dataset_generators = pytest.mark.parametrize(
    "ds_generator",
    ["local_ds_generator", "s3_ds_generator", "gcs_ds_generator"],
    indirect=True,
)


@pytest.fixture
def memory_ds(memory_path):
    return hub.dataset(memory_path)


@pytest.fixture
def local_ds(local_ds_generator):
    return local_ds_generator()


@pytest.fixture
def local_ds_generator(local_path):
    def generate_local_ds(**kwargs):
        return hub.dataset(local_path, **kwargs)

    return generate_local_ds


@pytest.fixture
def s3_ds(s3_ds_generator):
    return s3_ds_generator()


@pytest.fixture
def s3_ds_generator(s3_path):
    def generate_s3_ds(**kwargs):
        return hub.dataset(s3_path, **kwargs)

    return generate_s3_ds


@pytest.fixture
def gcs_ds(gcs_ds_generator):
    return gcs_ds_generator()


@pytest.fixture
def gcs_ds_generator(gcs_path, gcs_creds):
    def generate_gcs_ds():
        return hub.dataset(gcs_path, creds=gcs_creds)

    return generate_gcs_ds


@pytest.fixture
def hub_cloud_ds(hub_cloud_ds_generator):
    return hub_cloud_ds_generator()


@pytest.fixture
def hub_cloud_ds_generator(hub_cloud_path, hub_cloud_dev_token):
    def generate_hub_cloud_ds(**kwargs):
        return hub.dataset(hub_cloud_path, token=hub_cloud_dev_token, **kwargs)

    return generate_hub_cloud_ds


@pytest.fixture
def ds(request):
    """Used with parametrize to use all enabled dataset fixtures."""
    return request.getfixturevalue(request.param)


@pytest.fixture
def non_gcs_ds(request):
    """Used with parametrize to use all enabled dataset fixtures except gcs_ds."""
    return request.getfixturevalue(request.param)


@pytest.fixture
def ds_generator(request):
    """Used with parametrize to use all enabled persistent dataset generator fixtures."""
    return request.getfixturevalue(request.param)
