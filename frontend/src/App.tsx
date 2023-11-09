import {
  Admin,
  Resource,
  List, Datagrid, TextField,
  Create, SimpleForm, TextInput, FileInput, FileField
} from "react-admin";
import { dataProvider } from "./dataProvider";

const ImageList = () => (
  <List>
    <Datagrid>
      <TextField source="id" />
      <TextField source="tag" />
      <TextField source="size" label="Size (Bytes)" />
      <TextField source="created" />
    </Datagrid>
  </List>
);

const ImageCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="tag_name" />
      <FileInput source="dockerfile" placeholder={<p>Click to select your Dockerfile</p>}>
        <FileField source="src" title="title" />
      </FileInput>
    </SimpleForm>
  </Create>
);

export const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource
      name="images"
      list={ImageList}
      create={ImageCreate}
    />
  </Admin>
);
